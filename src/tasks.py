"""Tasks must be defined in a separate module due to the follow rq exception:

ValueError: Functions from the __main__ module cannot be processed by workers
"""


def tick(task):
    print(task)
