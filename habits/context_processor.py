from habits.models import Habit, HabitMember

def user_habits_context(request):
    context = HabitMember.objects.filter(user = request.user)
    return {'user_habits_context': context}

def all_habits_context(request):
    context = Habit.objects.all()
    return {'all_habits_context':context}