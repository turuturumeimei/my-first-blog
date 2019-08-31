from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
models.CharField 文字数が制限されたテキストを定義するフィールド
models.TextField これは制限なしの長いテキスト用
models.DateTimeField　日付と時間のフィールド
models.ForeignKey　ほかのモデルへのリンク
'''




