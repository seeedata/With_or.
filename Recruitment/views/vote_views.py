from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ..models import Question

@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 관심 목록에 넣을 수 없어요!')
    else:
        question.voter.add(request.user)
    return redirect('Recruitment:detail', question_id=question.id)