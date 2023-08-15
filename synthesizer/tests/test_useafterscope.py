import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from synthesizer import *
import config
import hashlib

class TestUseafterscope(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = './tmpdir_useafterscope'
        return super().setUp()
    def tearDown(self) -> None:
        if self._outcome.errors[-1][1] is None and len(self._outcome.result.failures) ==0:
            if os.path.exists(self.tmp_dir):
                shutil.rmtree(self.tmp_dir)
        return super().tearDown()
    
    def test_1(self):
        src_code_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test1.c'))
        oracle_files = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test1_oracle1.c')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test1_oracle2.c')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test1_oracle3.c'))
        ]
        oracle_md5 = []
        for oracle_f in oracle_files:
            with open(oracle_f, 'rb') as f:
                oracle = f.read().replace(b'\n', b'')
            oracle_md5.append(hashlib.md5(oracle).hexdigest())
        TOOL_STACKTOHEAP = f'{DYNAMIC_ANALYZER}/tool-stacktoheap --mutate-prob 0'
        ALL_TARGET_UB = [TargetUB.UseAfterScope]
        set_mut_md5 = []
        for _ in range(20): # due to randomness of synthesizer
            syner = Synthesizer(100, self.tmp_dir, TOOL_STACKTOHEAP, ALL_TARGET_UB)
            mutated_files = syner.synthesizer(src_code_file)
            for mut_src in mutated_files:
                with open(mut_src, 'rb') as f:
                    mut = f.read().replace(b'\n', b'')
                mut_md5 = hashlib.md5(mut).hexdigest()
                self.assertTrue(mut_md5 in oracle_md5)
                set_mut_md5.append(mut_md5)
                if len(set(set_mut_md5)) == len(set(oracle_md5)):
                    self.assertTrue(True)
                    return
        self.assertTrue(False)
    
    
    def test_2(self):
        src_code_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test2.c'))
        oracle_files = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test2_oracle1.c')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test2_oracle2.c')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test2_oracle3.c'))
        ]
        oracle_md5 = []
        for oracle_f in oracle_files:
            with open(oracle_f, 'rb') as f:
                oracle = f.read().replace(b'\n', b'')
            oracle_md5.append(hashlib.md5(oracle).hexdigest())
        TOOL_STACKTOHEAP = f'{DYNAMIC_ANALYZER}/tool-stacktoheap --mutate-prob 0'
        ALL_TARGET_UB = [TargetUB.UseAfterScope]
        set_mut_md5 = []
        for _ in range(20): # due to randomness of synthesizer
            syner = Synthesizer(100, self.tmp_dir, TOOL_STACKTOHEAP, ALL_TARGET_UB)
            mutated_files = syner.synthesizer(src_code_file)
            for mut_src in mutated_files:
                with open(mut_src, 'rb') as f:
                    mut = f.read().replace(b'\n', b'')
                mut_md5 = hashlib.md5(mut).hexdigest()
                self.assertTrue(mut_md5 in oracle_md5)
                set_mut_md5.append(mut_md5)
                if len(set(set_mut_md5)) == len(set(oracle_md5)):
                    self.assertTrue(True)
                    return
        self.assertTrue(False)
    
    
    def test_3(self):
        src_code_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test3.c'))
        oracle_files = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test3_oracle1.c')),
        ]
        oracle_md5 = []
        for oracle_f in oracle_files:
            with open(oracle_f, 'rb') as f:
                oracle = f.read().replace(b'\n', b'')
            oracle_md5.append(hashlib.md5(oracle).hexdigest())
        TOOL_STACKTOHEAP = f'{DYNAMIC_ANALYZER}/tool-stacktoheap --mutate-prob 0'
        ALL_TARGET_UB = [TargetUB.UseAfterScope]
        set_mut_md5 = []
        for _ in range(20): # due to randomness of synthesizer
            syner = Synthesizer(100, self.tmp_dir, TOOL_STACKTOHEAP, ALL_TARGET_UB)
            mutated_files = syner.synthesizer(src_code_file)
            for mut_src in mutated_files:
                with open(mut_src, 'rb') as f:
                    mut = f.read().replace(b'\n', b'')
                mut_md5 = hashlib.md5(mut).hexdigest()
                self.assertTrue(mut_md5 in oracle_md5)
                set_mut_md5.append(mut_md5)
                if len(set(set_mut_md5)) == len(set(oracle_md5)):
                    self.assertTrue(True)
                    return
        self.assertTrue(False)
    
    def test_4(self):
        src_code_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test4.c'))
        oracle_files = [
        ]
        oracle_md5 = []
        for oracle_f in oracle_files:
            with open(oracle_f, 'rb') as f:
                oracle = f.read().replace(b'\n', b'')
            oracle_md5.append(hashlib.md5(oracle).hexdigest())
        TOOL_STACKTOHEAP = f'{DYNAMIC_ANALYZER}/tool-stacktoheap --mutate-prob 0'
        ALL_TARGET_UB = [TargetUB.UseAfterScope]
        for _ in range(4): # due to randomness of synthesizer
            syner = Synthesizer(100, self.tmp_dir, TOOL_STACKTOHEAP, ALL_TARGET_UB)
            mutated_files = syner.synthesizer(src_code_file)
            self.assertTrue(len(mutated_files)==0)
    
    def test_5(self):
        src_code_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcases/useafterscope/test5.c'))
        oracle_files = [
        ]
        oracle_md5 = []
        for oracle_f in oracle_files:
            with open(oracle_f, 'rb') as f:
                oracle = f.read().replace(b'\n', b'')
            oracle_md5.append(hashlib.md5(oracle).hexdigest())
        TOOL_STACKTOHEAP = f'{DYNAMIC_ANALYZER}/tool-stacktoheap --mutate-prob 0'
        ALL_TARGET_UB = [TargetUB.UseAfterScope]
        for _ in range(4): # due to randomness of synthesizer
            syner = Synthesizer(100, self.tmp_dir, TOOL_STACKTOHEAP, ALL_TARGET_UB)
            mutated_files = syner.synthesizer(src_code_file)
            self.assertTrue(len(mutated_files)==0)
            

if __name__ == '__main__':
    unittest.main()