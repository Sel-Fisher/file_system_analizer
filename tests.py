import os
import shutil
import tempfile
import unittest
from unittest.mock import patch
from file_system_analyzer import classify_file_type, analyze_directory


class TestFileSystemAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.txt")
        with open(self.test_file, "w") as f:
            f.write("Test file content")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        shutil.rmtree(self.test_dir)

    def test_classify_file_type(self):
        self.assertEqual(classify_file_type(self.test_file), "text")

        # Add more file types to test
        image_file = os.path.join(self.test_dir, "test.jpg")
        with open(image_file, "w") as f:
            f.write("Not a real image")
        self.assertEqual(classify_file_type(image_file), "image")

    @patch("builtins.print")
    def test_analyze_directory(self, mock_print):
        # Test analyze_directory with a small file
        analyze_directory(self.test_dir, size_threshold=1024)
        mock_print.assert_called_with(
            f"There is no files larger than {1024 / 1024 / 1024:.2f} MB"
        )

        # Test analyze_directory with a large file
        large_file = os.path.join(self.test_dir, "large_file.txt")
        with open(large_file, "wb") as f:
            f.write(b"0" * 1048577)  # 1 MB + 1 byte
        analyze_directory(self.test_dir, size_threshold=1024)
        mock_print.assert_any_call(f"{large_file}: 1.00 MB")

    @patch("builtins.print")
    def test_analyze_directory_world_writable(self, mock_print):
        # Test analyze_directory with a world-writable file
        world_writable_file = os.path.join(self.test_dir, "world_writable.txt")
        with open(world_writable_file, "w") as f:
            f.write("World-writable file")
        os.chmod(world_writable_file, 0o777)
        analyze_directory(self.test_dir, size_threshold=0, show_world_writable=True)
        mock_print.assert_any_call(world_writable_file)


    def test_analyze_directory_nested_directories(self):
        # Test with a directory structure that includes nested directories
        nested_dir = os.path.join(self.test_dir, "nested")
        os.makedirs(nested_dir)
        nested_file = os.path.join(nested_dir, "nested_file.txt")
        with open(nested_file, "w") as f:
            f.write("Nested file")
        analyze_directory(self.test_dir, size_threshold=0)
