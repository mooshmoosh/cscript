# cscript
Write scripts in C. No boilerplate. Define functions where ever you like.

This is my own take on [c](https://github.com/ryanmjacobs/c).

# Installing

```
  git clone git@github.com:mooshmoosh/cscript.git
  cd cscript
  sudo ./install.sh
```

# Example

Put the following in a file called helloworld.c

```
  #!/usr/bin/cscript
  printf("Hello world!\n");
```
  
Make the file executable, and then run it:

```
  $ chmod +x helloworld.c
  $ ./helloworld.c
  Hello world
```

# Using shared libraries

You can pass arguments to gcc by adding them to the "--compiler-arguments" parameter in the shebang. This is illustrated in the curltest.c example.

```
  #!/usr/bin/cscript --compiler-arguments="-lcurl"
  #include <curl/curl.h>

  CURL *curl;
  CURLcode res;

  curl = curl_easy_init();
  if(!curl) {
      printf("Could not initialise curl\n");
      return 1;
  }

  curl_easy_setopt(curl, CURLOPT_URL, "http://example.com");
  curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
  res = curl_easy_perform(curl);
  if(res != CURLE_OK)
    fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

  curl_easy_cleanup(curl);

```

# Function and type definitions

Any functions and typedef statements will be hoisted to the top of the file. This means you can declare functions near where they are used. You can write code like this:

```
  #!/usr/bin/cscript
  
  int x = 5;

  int square(int param)
  {
      return param * param;
  }
  
  printf("x squared = %d\n", square(x));
```
