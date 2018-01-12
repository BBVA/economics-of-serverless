import awscosts


def test_init():
    my_lambda = awscosts.Lambda()
    assert my_lambda.mem == 128


def test_non_standard_mem():
    my_lambda = awscosts.Lambda(MB_per_req=250)
    assert my_lambda.mem == 256


def test_no_free_tier():
    my_lambda_nofree = awscosts.Lambda(use_free_tier=False)
    assert my_lambda_nofree.free_tier == (0, 0)


def test_costs_non_free():
    my_lambda_nofree = awscosts.Lambda(use_free_tier=False)
    my_lambda = awscosts.Lambda()
    reqs = 1000000
    cost1 = my_lambda.get_cost(reqs)
    cost2 = my_lambda_nofree.get_cost(reqs)
    assert cost1 < cost2, 'Cost1 {} < cost2 {}'.format(cost1, cost2)


def test_costs_free():
    my_lambda = awscosts.Lambda()
    reqs = 100
    cost = 0
    while cost < 1:
        cost += my_lambda.get_cost(reqs)
        reqs += reqs
    assert reqs == 6553600, 'Requests needed to get 1$: {}'.format(reqs)
