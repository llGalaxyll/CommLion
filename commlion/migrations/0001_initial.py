# Generated by Django 3.2 on 2021-07-02 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uni',
            fields=[
                ('uni_num', models.IntegerField(primary_key=True, serialize=False)),
                ('uni_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('student_password', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=20)),
                ('student_generation', models.CharField(max_length=3)),
                ('uni_num', models.ForeignKey(db_column='uni_num', on_delete=django.db.models.deletion.CASCADE, to='commlion.uni')),
            ],
        ),
        migrations.CreateModel(
            name='SessionPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_year', models.IntegerField()),
                ('session_num', models.IntegerField()),
                ('session_title', models.CharField(max_length=30)),
                ('session_file', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('session_content', models.TextField()),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='commlion.student')),
            ],
        ),
        migrations.CreateModel(
            name='QnaPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('hashtag1', models.CharField(max_length=15)),
                ('hashtag2', models.CharField(max_length=15)),
                ('file', models.ImageField(blank=True, null=True, upload_to='QnaImage/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(default=0)),
                ('session_id', models.ForeignKey(db_column='session_id', on_delete=django.db.models.deletion.CASCADE, to='commlion.sessionpost')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='ProjectImage/')),
                ('title', models.CharField(max_length=30)),
                ('introduction', models.TextField()),
                ('developer', models.TextField()),
                ('dev_period', models.CharField(max_length=30)),
                ('dev_stack', models.CharField(max_length=50)),
                ('ref', models.TextField()),
                ('state', models.CharField(max_length=5)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('uni_num', models.ForeignKey(db_column='uni_num', on_delete=django.db.models.deletion.CASCADE, to='commlion.uni')),
            ],
        ),
        migrations.CreateModel(
            name='NoticePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='commlion.student')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('like_num', models.IntegerField(default=0)),
                ('qna_id', models.ForeignKey(db_column='qna_id', on_delete=django.db.models.deletion.CASCADE, to='commlion.qnapost')),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='commlion.student')),
            ],
        ),
    ]
