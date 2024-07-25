def temp():
  tmp = '''
  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Simple Flask Input Box</title>
    </head>
    <body>
      <h1>Enter Your Input</h1>
      <form method="post" action="/">
        <label for="user_input">Input:</label>
        <input type="text" id="user_input" name="user_input" required>
        <input type="submit" value="Submit">
      </form>
      {% if user_input %}
        <h2>You entered: {{ user_input }}</h2>
      {% endif %}
    </body>
  </html>
  '''
  return tmp