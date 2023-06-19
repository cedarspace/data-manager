# tests/test_rptodo.py
import sys 
import os
import check_output

sys.path.insert(1, '../')

from unittest import TestCase
from data_manager import cli


class TryTesting(TestCase):
    '''project-creator testing'''
    def test_project_creator_true(self):
        self.assertTrue(cli.project_creator("loda1", "../", cli.ProjectCreatorArgs(3, ["source1", 'source2', 'source3'], 2, ["model1", "model2"])))
    def test_project_creator_1_2(self):
        self.assertEqual(cli.project_creator("loda2", "/Users/cedarspace/Deskto", cli.ProjectCreatorArgs(3, ["source1", 'source2', 'source3'], 2, ["model1", "model2"])), 2)
    def test_project_creator_3(self):
        self.assertEqual(cli.project_creator("loda4", "../", cli.ProjectCreatorArgs(4, ["source1", 'source2', 'source3'], 1, ["model1", "model2"])), 3)
    '''file-mover testing'''
    def test_file_mover_dc(self):
        os.makedirs("/Users/cedarspace/Desktop/test1")
        self.assertTrue(cli.file_mover('/Users/cedarspace/Desktop/loda', '/Users/cedarspace/Desktop/test1', '1.data_collection'))
        os.removedirs("/Users/cedarspace/Desktop/loda/1.data_collection/test1")
    def test_file_mover_training(self):
        os.makedirs("/Users/cedarspace/Desktop/test2")
        self.assertTrue(cli.file_mover('/Users/cedarspace/Desktop/loda', '/Users/cedarspace/Desktop/test2', '2.training'))
        os.removedirs("/Users/cedarspace/Desktop/loda/2.training/test2")
    def test_file_mover_eval(self):
        os.makedirs("/Users/cedarspace/Desktop/test3")
        self.assertTrue(cli.file_mover('/Users/cedarspace/Desktop/loda', '/Users/cedarspace/Desktop/test3', '3.evaluation'))
        os.removedirs("/Users/cedarspace/Desktop/loda/3.evaluation/test3")
    def test_file_mover_deploy(self):
        os.makedirs("/Users/cedarspace/Desktop/test4")
        self.assertTrue(cli.file_mover('/Users/cedarspace/Desktop/loda', '/Users/cedarspace/Desktop/test4', '4.deployment'))
        os.removedirs("/Users/cedarspace/Desktop/loda/4.deployment/test4")
    def test_file_mover_1_stage(self):
        self.assertEqual(cli.file_mover('/Users/cedarspace/Desktop/loda', '/Users/cedarspace/Desktop/test4', '4.depoyment'), 1)
    def test_file_mover_1_project(self):
        self.assertEqual(cli.file_mover('/Users/cedarspace/Desktop/lod', '/Users/cedarspace/Desktop/test4', '4.depoyment'), 1)
    def test_file_mover_1_file(self):
        self.assertEqual(cli.file_mover('/Users/cedarspace/Desktop/loda', '/Users/cedarspace/Desktop/test', '4.depoyment'), 1)
    '''file namer testing '''
    def test_file_namer_spaces(self):
        self.assertEqual(cli.file_namer("test test "), "test_test_")
    def test_file_namer_special_charc(self):
        self.assertEqual(cli.file_namer("!@#foo%^$"), "foo")
    def test_file_namer_capital(self):
        self.assertEqual(cli.file_namer("EXAM"), "exam")
    def test_file_namer_combo(self):
        self.assertEqual(cli.file_namer("let-it@-snow why Not!"), "let_it_snow_why_not")
    ''''''


