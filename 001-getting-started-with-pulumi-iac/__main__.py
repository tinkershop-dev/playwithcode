"""An AWS Python Pulumi program"""

import pulumi
from pulumi_random import RandomPassword, RandomPasswordArgs

my_password = RandomPassword("my-password", RandomPasswordArgs(
    length=32,
    keepers={
      "seed": "seed 1",
    },
))

pulumi.export("password-value", my_password.result)