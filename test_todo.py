import unittest
from unittest.mock import patch, mock_open
import argparse
import json
from script import load_tasks, save_tasks, task_file

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.test_file = "tasks.json"
        self.mock_data = [
            {
                "id": 0,
                "description": "Test task 1",
                "status": "TODO",
                "createdAt": "2023-01-01T00:00:00",
                "updatedAt": "2023-01-01T00:00:00"
            },
            {
                "id": 1,
                "description": "Test task 2",
                "status": "IN_PROGRESS",
                "createdAt": "2023-01-02T00:00:00",
                "updatedAt": "2023-01-02T00:00:00"
            }
        ]

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([]))
    def test_load_tasks_empty(self, mock_file):
        tasks = load_tasks()
        self.assertEqual(tasks, [])
        mock_file.assert_called_once_with(self.test_file, 'r')

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([]))
    def test_load_tasks_with_data(self, mock_file):
        mock_file.return_value.read.return_value = json.dumps(self.mock_data)
        tasks = load_tasks()
        self.assertEqual(tasks, self.mock_data)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        save_tasks(self.mock_data)
        mock_file().write.assert_called_once_with(json.dumps(self.mock_data))

    def test_add_task(self):
        tasks = []
        new_task = {
            "id": 2,
            "description": "New Task",
            "status": "TODO",
            "createdAt": "2023-01-03T00:00:00",
            "updatedAt": "2023-01-03T00:00:00"
        }
        tasks.append(new_task)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "New Task")

    def test_list_tasks(self):
        tasks = self.mock_data
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["description"], "Test task 1")

    def test_update_task(self):
        tasks = self.mock_data
        tasks[1]['description'] = "Updated Task"
        self.assertEqual(tasks[1]["description"], "Updated Task")

    def test_delete_task(self):
        tasks = self.mock_data.copy()
        tasks.pop(1)  # Remove the second task
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task 1")

    def test_mark_task_done(self):
        tasks = self.mock_data
        tasks[0]['status'] = 'Done'
        self.assertEqual(tasks[0]["status"], 'Done')

if __name__ == "__main__":
    unittest.main()
