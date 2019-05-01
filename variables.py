from datetime import datetime

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'First blog post',
        'content': 'Hello world, this is cs50',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second blog post',
        'content': 'I am learning flask.',
        'date_posted': 'April 21, 2018'
    }
]

yearNow=datetime.now().year
