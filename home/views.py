from django.shortcuts import render

tasks = ["phone", "phone1"]

def index(request):
    if (request.method == "POST"):
        task = request.POST.get('task')
        tasks.append(task)

    return render(request, "home/index.html", {
        "tasks" : tasks
})

