# swissarmy-site
A repo containing several python scripts that allow you to create sitemaps, and extract info about files on your local computer. Designed with archiving and netart communities in mind. 

There are currently three scripts available to the user.

### extract_folder
  This creates a general_info.json file that will list all of the file types found in a given folder and their corresponding locations. 
  
  This can be useful for figuring out what file types exist in an enormous archive or unexamined netart repo
  Example
  ```
  {
    "html":[
    "/Users/example_user/index.html",
    "/Users/example_user/travel.html",
    "/Users/example_user/faq.html"
    ],
    
    "DS_Store":[
    "/Users/example_user/.DS_Store",
    "/Users/example_user/img/.DS_Store"
    ],
    
    "ttf":[
    "/Users/example_user/Puritan.ttf",
    "/Users/example_user/Puritan-Italic.ttf"
    ]
  }
```

### extract_page
  This creates a PASSED_FILE_NAME_info.json file that will list all of the images, href links, script sources, and link tags found in a passed html file
  
  This can be useful for recording in an external shorthand what a html page references
  
  Example
  ```
  {
    "a_tag":[
      "index.html",
      "travel.html",
      "faq.html"
      ],
    "link_tag":[
      "css/materialize.css",
      "css/style.css",
      "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css",
      "https://fonts.googleapis.com/icon?family=Material+Icons"
    ],
  "img":[
    "img/background1.jpg",
    "img/wagon.svg",
    "img/cat.svg",
    "img/quill.svg"
  ],
  "scripts":[
    "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js",
    "https://code.jquery.com/jquery-2.1.1.min.js",
    "js/materialize.js",
    "js/init.js"
  ]
}
```
### sitemap_helper
  This creates a PASSED_FILENAME_sitemap.xml file that shows the location of all linked sites and their last changed date
  
  This can be useful for creating sitemaps for personal projects or locally hosted code
 
## Running the scripts

### extract_folder
```python3 extract_folder.py FULL_PATH```

### extract_page
```python3 extract_page.py FULL_PATH/index.html```

### sitemap_helper
```python3 sitemap_helper.py FULL_PATH/index.html```


