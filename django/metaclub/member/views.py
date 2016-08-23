from django.shortcuts import render, get_object_or_404
from member.models import Staff, Student
from django.views import generic
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse


class ViewList(generic.ListView):
    # Display a list of all the member
    model = Student
    template_name = 'member/list.html'
    context_object_name = 'students'

    def dispatch(self, *args, **kwargs):
        return super(ViewList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewList, self).get_context_data(**kwargs)
        context['myVariableOfContext'] = 0

        return context


class ViewStudent(generic.DetailView):
    # Display a information about a student
    model = Student
    template_name = 'member/view.html'
    context_object_name = "student"

    def dispatch(self, *args, **kwargs):
        return super(ViewStudent, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewStudent, self).get_context_data(**kwargs)
        context['myVariableOfContext'] = 0


class CreateStudent(generic.CreateView):
    # Create a new student
    model = Student
    template_name = 'member/create.html'
    context_object_name = "student"

    def dispatch(self, *args, **kwargs):
        return super(CreateStudent, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateStudent).get_context_data(**kwargs)
        context['myVariableOfContext'] = 0


def delete_member():
    pass


def UpdateMember():
    pass
