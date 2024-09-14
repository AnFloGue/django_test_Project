from django.views.generic.edit import FormView
from .forms import TeacherForm

class TeacherFormView(FormView):
    template_name = 'teacher_form.html'
    form_class = TeacherForm
    success_url = '/success/'

    def form_valid(self, form):
        # Process the form data here
        return super().form_valid(form)