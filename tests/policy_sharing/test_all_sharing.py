import unittest
from marllib import marl


class TestMAgentEnv(unittest.TestCase):

    def test_all_sharing(self):
        for algo_name in dir(marl.algos):
            if "_" not in algo_name:
                if algo_name in ["ddpg", "maddpg", "facmac"]:
                    env = marl.make_env(environment_name="mpe", map_name="simple_spread",
                                        continuous_actions=True)
                    algo = getattr(marl.algos, algo_name)(hyperparam_source="test")
                    model = marl.build_model(env, algo, {"core_arch": "mlp", "encode_layer": "16-16"})
                    algo.fit(env, model, stop={"training_iteration": 3}, local_mode=False, num_gpus=0,
                             num_workers=2, share_policy="all", checkpoint_end=False)
                elif algo_name in ["happo", "hatrpo"]:
                    continue
                else:
                    env = marl.make_env(environment_name="mpe", map_name="simple_spread",
                                        continuous_actions=False)
                    algo = getattr(marl.algos, algo_name)(hyperparam_source="test")
                    model = marl.build_model(env, algo, {"core_arch": "mlp", "encode_layer": "16-16"})
                    algo.fit(env, model, stop={"training_iteration": 3}, local_mode=False, num_gpus=0,
                             num_workers=2, share_policy="all", checkpoint_end=False)


if __name__ == "__main__":
    import pytest
    import sys

    sys.exit(pytest.main(["-v", __file__]))