WORKING_DIR='./dist'
if [ -d "$WORKING_DIR" ]; then rm -Rf $WORKING_DIR; fi
mkdir ./dist

# copy images
cp -a ./source/img/ $WORKING_DIR/img/

# copy css
cp -a ./style/ $WORKING_DIR/style/

python3 app.py

# resize png and jpg images
#convert  -resize 450 "./dist/img/*.jpg" -set filename:base "%[basename]" "./dist/img/%[filename:base].jpg"
#convert  -resize 450 "./dist/img/*.png" -set filename:base "%[basename]" "./dist/img/%[filename:base].png"
ls
pwd
cd $WORKING_DIR && find . -name '*.jpg' -execdir mogrify -resize 450 {} + && find . -name '*.png' -execdir mogrify -resize 450 {} +
