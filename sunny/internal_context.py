"""
This module is meant for internal purpose use only
This module is internally used to schedule and run the task and workers
"""

class _DefaultScheduler(object):

    def create_local_scheduler(self):
        return scheduler.Scheduler(prune_after_work = True)
    def create_worker(self , scheduler , worker_processes):
        return worker.Worker(scheduler = scheduler , worker_processes = worker_processes)


def _schedule_and_run(tasks , worker_scheduler = None , worker_processes,parallel_scheduling) :
    """
    :param tasks tasks to be scheduled
    :worker_scheduler = local scheduler or userdefined
    """
    if worker_scheduler is None:
        worker_scheduler = _DefaultScheduler()
    scheduler = worker_scheduler.create_local_scheduler()
    worker = worker_scheduler.create_worker(scheduler = scheduler , worker_processes = worker_processes)
    success = True
    with worker:
        for t in tasks:
            success &= worker.add(t  , parallel_scheduling)
        success &= worker.run()
    #TODO:Execution Summary

def run(tasks , worker_scheduler = None , worker_processes = 1 , parallel_scheduling = False):
    """
    Run the tasks with the help of the scheduler
    :param tasks
    :para, worker_scheduler
    """
    _schedule_and_run(tasks , worker_scheduler , worker_processes , parallel_scheduling)
    #TODO: Return the status over here


