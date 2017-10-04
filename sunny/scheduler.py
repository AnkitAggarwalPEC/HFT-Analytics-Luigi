"""
This is used to handle the various workers

"""

class SchedulerParameters(config):
    retry_delay = config.get("retry_delay")
    state_path = config.get("state_path")
    batch_emails = config.get("batch_emails")
    record_task_history = config.get("record_task_history")
    prune_on_get_work = config.get("prune_on_get_work")

class SchedulerState(object):

    def __init__(self,  state_path):
        self._state_path = state_path
        self._tasks = {}
        self._status_tasks = {}
        self._active_workers = {}

    def get_scheduler_state(self):
        return  self._tasks , self._status_tasks , self._active_workers

    def set_scheduler_state(self , new_tasks , new_status_task , new_active_workers):
        self._tasks = new_tasks
        self._status_tasks = new_status_task
        self._active_workers = new_active_workers

    def get_active_tasks(self):
        return self._tasks

    def get_task_status(self):
        return self._status_tasks

    def get_task(self ,task_id , default = None , set_default = None):
        if set_default:
            DO SOMETHING
        else:
            return self._tasks.get(task_id , default)

    def set_task_status(self , task , new_status , config = None):
        if new_status == DISABLED and task.status == RUNNING:
            return
        if new_status  != task.status:
            self._status_tasks[task.status].pop(task.id)
            self._status_tasks[new_status][task.id] = task

    def get_active_worker():
        return self._active_workers

    def get_worker(self , worker_id):
        return self._active_workers.get(worker_id , WorkerTracker(worker_id))

class WorkerTracker(object):
    """
    Structure for tracking the worker activity
    """
    def __init__(self , worker_id):
        self.id = worker_id
        self.tasks = set()
        self.can_work = True



class Scheduler(object):
    """
    """
    def __init__(self , config = None , resources = None , task_history_impl = None , **kwargs):
        """
        """
        self._config = config or SchedulerParameters(**kwargs)
        self._state = SchedulerState(self._config.state_path)

    def _update_worker(self , worker_id):
        worker = self._state.get_worker(worker_id)
        return worker

    def add_task(self , task_id= None , status = PENDING , deps = None , resources = None , worker_id = None , priority = None):

        assert worker_id in not None
        worker = self._update_worker(worker_id)

        if worker.can_work:
            _task_for_this_worker = Tasks( task_id = task_id , status= PENDING , deps = deps , resources = resources ,priority = priority)
            self._state.get_task(task_id , _task_for_this_worker)
        else:
            _task_for_this_worker = None








