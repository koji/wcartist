# wcartust

## How to use
1. create a text file   
   
![](https://github.com/koji/wcartist/blob/master/image/input.png)   
   
     
2. get an black & white image     
3. run command     
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
![output](https://github.com/koji/wcartist/blob/master/image/output.png)
