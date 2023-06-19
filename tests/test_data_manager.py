# tests/test_rptodo.py
import sys 
import os
import check_output

sys.path.insert(1, '../')

from unittest import TestCase
from data_manager import cli

class TryTesting(TestCase):
    def test_project_creator_true(self):
        self.assertTrue(cli.project_creator("loda1", "../", cli.ProjectCreatorArgs(3, ["source1", 'source2', 'source3'], 2, ["model1", "model2"])))
    def test_project_creator_1_2(self):
        self.assertEqual(cli.project_creator("loda2", "/Users/cedarspace/Deskto", cli.ProjectCreatorArgs(3, ["source1", 'source2', 'source3'], 2, ["model1", "model2"])), 2)
    def test_project_creator_3(self):
        self.assertEqual(cli.project_creator("loda4", "../", cli.ProjectCreatorArgs(4, ["source1", 'source2', 'source3'], 1, ["model1", "model2"])), 3)
    def test_file_mover_dc(self):
        self.assertTrue(cli.file_mover('/Users/cedarspace/Documents/GitHub/loda3', '/Users/cedarspace/Desktop/test1', '1.data_collection'))
    def test_file_mover_training(self):
        self.assertTrue(cli.file_mover('/Users/cedarspace/Documents/GitHub/loda3', '/Users/cedarspace/Desktop/test2', '2.training'))
    def test_file_mover_eval(self):
        self.assertTrue(cli.file_mover('/Users/cedarspace/Documents/GitHub/loda3', '/Users/cedarspace/Desktop/test3', '3.evaluation'))
    def test_file_mover_deploy(self):
        self.assertTrue(cli.file_mover('/Users/cedarspace/Documents/GitHub/loda3', '/Users/cedarspace/Desktop/test4', '4.deployment'))
    def test_file_mover_1(self):
        self.assertEqual(cli.file_mover('/Users/cedarspace/Documents/GitHub/loda3', '/Users/cedarspace/Desktop/test4', '4.depoyment'), 1)
        