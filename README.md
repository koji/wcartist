# wcartist

## How to install
```
$ pip install wcartist
```

```
$ git clone https://github.com/koji/wcartist.git
$ cd wcartist/code 
$ pip install setuptools
$ python setup.py install  this requires setuptools > 38.0.0
```

## How to use
### 1. create a text file        
### 2. get an black & white image
### 3. run command     
```
$ wcartist --input image.png --text test.txt --num 1000 --bc black --output wcartist
```

`options`     
```
--input: image_file_name (required)
--text: text file name (required)
--num: words max default=500 (optional)
--bc: background color default `white` (optional)
`black`, `red`, `blue`, `green`, `orange`, `purple`
`cyan`, `gray`, `brown`, `pink`, `yellow`, `silver`
`gold`, `darkblue` etc
--output: output file name default `output` (optional)
```

## example
![input](https://github.com/koji/wcartist/blob/master/image/input.png) 
![output](https://github.com/koji/wcartist/blob/master/image/output.png)

![comparison](https://github.com/koji/wcartist/blob/master/image/wcartist_sample01.png)
