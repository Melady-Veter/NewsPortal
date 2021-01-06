from news.models import *
User.objects.create(username='Alex', password='12345')
<User: Alex>
User.objects.create(username='Mike', password='23456')
<User: Mike>
Author.objects.create(author=User.objects.get(id=3))
<Author: Mike>
 Author.objects.create(author=User.objects.get(id=2))
<Author: Alex>
Category.objects.create(name='Городские новости')
<Category: Городские новости>
Category.objects.create(name='Спорт')
<Category: Спорт>
Category.objects.create(name='Политика')
<Category: Политика>
Category.objects.create(name='Погода')
<Category: Погода>
Post.objects.create(author=Author.objects.get(id=2), type = 'NW',
                    header= 'Интересненькая новость',
                    article_text='Новость о том какая поода в городе')
<Post: Интересненькая новость>
Post.objects.create(author=Author.objects.get(id=2), type = 'AR',
                    header= 'Большая статья',
                    article_text='Текст большой статьи')
<Post: Большая статья>
Post.objects.create(author=Author.objects.get(id=2), type = 'AR',
                    header= 'Маленькая статейка',
                    article_text='Текст маленькой статейки')
<Post: Маленькая статейка>
post = Post.objects.get(id=1)
city = Category.objects.get(id=1)
PostCategory.objects.create(post=post, category = city)
<PostCategory: Городские новости>
post = Post.objects.get(id=1)
weather = Category.objects.get(id=4)
PostCategory.objects.create(post=post, category = weather)
<PostCategory: Погода>
post = Post.objects.get(id=2)
sport = Category.objects.get(id=2)
PostCategory.objects.create(post=post, category = sport)
<PostCategory: Спорт>
post = Post.objects.get(id=3)
politika = Category.objects.get(id=3)
PostCategory.objects.create(post=post, category = politika)
<PostCategory: Политика>
author = User.objects.get(id=2)
post = Post.objects.get(id=1)
Comment.objects.create(post=post, author=author, text='Текст первого комментария')
<Comment: Alex - 1>
author = User.objects.get(id=3)
post = Post.objects.get(id=1)
Comment.objects.create(post=post, author=author, text='Текст второго комментария')
<Comment: Mike - 2>
author = User.objects.get(id=3)
post = Post.objects.get(id=2)
Comment.objects.create(post=post, author=author, text='Текст третьего комментария')
<Comment: Mike - 3>
author = User.objects.get(id=2)
post = Post.objects.get(id=3)
Comment.objects.create(post=post, author=author, text='Текст четвёртого комментария')
<Comment: Alex - 4>

# Ставим лайки комментариям
comments = Comment.objects.all()
comments[6].like() # 3 лайка для Тома Круза

# Ставим лайки для поста
post.like()

# меняем рейтинг посту
post.post_raiting = 100
post.save()

# Обновляем рейтинги авторов
for auth in Author.objects.all():
    auth.update_raiting()

Author.objects.all().order_by('-author_raiting').values('author__username','author_raiting')[0]

best = Post.objects.all().order_by('-post_raiting')[0]
best_post= Post.objects.all().order_by('-post_raiting').values( # выводим параметры
    'created_time',
    'author__author__username',
    'header', 'post_raiting',
    'article_text')[0]
best.preview()

