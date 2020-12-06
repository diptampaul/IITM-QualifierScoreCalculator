# IITM-QualifierScoreCalculator

Tutorial on How to Use it: https://www.youtube.com/watch?v=DGDUvxNFZ4M&feature=youtu.be

Sample Secret Key I used in this video: 'b9(m(hxt=019n*k+#q1+$ap29-+ce9%fh&bznhpvd7e88tg*$j'

copy and paste it in the settings

First go into the IITM folder, there run

pip install -r requirements.txt

then after changing secret key in the settings.py

run python ./manage.py/ migrate

Then, python ./manage.py/ collectstatic

And Lastly, python ./manage.py/ runserver



To check the database, run,

python ./manage.py/ dbshell
to check tables write
.tables while u r inside the dbshell

And to check the datas inside the table run

SELECT * FROM upload_fileupload
