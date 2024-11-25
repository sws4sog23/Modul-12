import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        wolk_t = runner.Runner('Ходьба')
        for i in range(10):
            wolk_t.walk()
        ww = wolk_t.distance
        self.assertEqual(ww, 50)

    def test_run(self):
        run_t = runner.Runner('Бег')
        for i in range(10):
            run_t.run()
        rr = run_t.distance
        self.assertEqual(rr, 100)

    def test_challenge(self):
        wolk_t1 = runner.Runner('Ходьба')
        run_t1 = runner.Runner('Бег')
        for i in range(10):
            wolk_t1.walk()
            run_t1.run()
        rr1 = run_t1.distance
        ww1 = wolk_t1.distance
        self.assertNotEqual(ww1, rr1)

if __name__ == "__main__":
    unittest.main()




