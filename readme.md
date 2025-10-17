# 1. First, install the necessary libraries:

>>> pip install fastapi "uvicorn[standard]"

# 2. Now, run your app from the terminal:

>>> uvicorn main:app --reload

## or if folder , then folder_name.main:app --reload

>>> uvicorn Basic.main:app --reload

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```