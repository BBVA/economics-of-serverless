import awscosts
import pytest


def test_no_params():
    with pytest.raises(ValueError):
        awscosts.EC2("t2.micro")

    with pytest.raises(ValueError):
        awscosts.EC2("t2.micro", ms_per_req=200)

    with pytest.raises(ValueError):
        awscosts.EC2("t2.micro", MB_per_req=200)


def test_init_1():
    t2micro = awscosts.EC2('t2.micro', max_reqs_per_second=200)
    assert t2micro.max_reqs_per_second == 200


def test_max_reqs():
    t2micro = awscosts.EC2('t2.micro', ms_per_req=200, MB_per_req=1024)
    assert t2micro.max_reqs_per_second == 5


def test_scalability():
    max_reqs = 200
    t2micro = awscosts.EC2('t2.micro', max_reqs_per_second=max_reqs)
    assert t2micro.get_num_instances(max_reqs + 1) == 2
