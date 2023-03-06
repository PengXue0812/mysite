
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    # template_name属性用于告诉Django使用一个指定的模板名字来渲染模板,用于替换默认的<app name>/<model name>_list.html
    template_name = 'polls/index.html'
    # 自动生成的上下文变量question_list的名字改为latest_question_list
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    # template_name属性用于告诉Django使用一个指定的模板名字来渲染模板,用于替换默认的<app name>/<model name>_detail.html
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#  from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse 

# from .models import Choice, Question

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     # render()函数第一个位置参数是请求对象request, 第二个参数是模板文件。第三个参数是一个可选的字典，包含需要传递给模板的数据
#     # 最后render函数返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象
#     return render(request, 'polls/index.html', context)

# # 注意函数的参数
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#     # question = get_object_or_404(Question, pk=question_id)
#     # return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     # get_object_or_404()方法将一个Django模型作为第一个位置参数，后面可以跟任意数量的关键字参数，如果对象不存在则弹出Http404异常
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST：一个类似字典的对象，允许通过键名访问提交的数据。
        # 本例中，request.POST['choice]返回被选择选项的ID值，并且值的类型永远是string字符串
        # 同样，可以通过获取request.GET['choice']GET请求的数据
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 如果POSt数据里没有提供choice键值，request.POST['choice']有可能触发一个KeyError异常。这种情况下，上面的代码会返回表单页面并给出错误提示
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question, 
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 在选择计数器加1后，需要返回一个HttpResponseRedirect
        # HttpResponseRedirect需要一个参数：重定向的URL
        # HttpResponseRedirect的构造器中使用了一个reverse()函数，能避免在视图函数中硬编码URL
        # 首先需要一个我们在URLconf中指定的name，然后是传递的数据
        # 重定向后，浏览器会发起一个新的请求，而不是使用原始请求的数据
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))