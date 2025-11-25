from django.shortcuts import get_object_or_404
from .models import Task
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm

class TaskList(LoginRequiredMixin,TemplateView):
    template_name="tasks/tasks_list.html"
    
class TaskDetail(LoginRequiredMixin,TemplateView):
    template_name="tasks/task_detail.html"
    
class TaskCreate(LoginRequiredMixin,TemplateView):
    template_name = "tasks/task_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form_title"] = "Create Task"
        ctx["submit_text"] = "Create Task"
        ctx["task_id"] = None  
        ctx["form"]=TaskForm()
        return ctx


class TaskUpdate(LoginRequiredMixin,TemplateView):
    template_name = "tasks/task_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        task_id = kwargs.get("pk")

        # Optional: ensure task exists (avoids broken page)
        get_object_or_404(Task, pk=task_id)

        ctx["form_title"] = "Update Task"
        ctx["submit_text"] = "Save Changes"
        ctx["task_id"] = task_id 
        ctx["form"]=TaskForm()
        return ctx
    
class TaskDelete(LoginRequiredMixin,TemplateView):
    template_name = "task_confirm_delete.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        task_id = kwargs.get("pk")

        task = get_object_or_404(Task, pk=task_id)
        ctx["task"] = task
        ctx["task_id"] = task_id

        return ctx
