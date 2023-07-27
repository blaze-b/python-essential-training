# Python Manage Complex Packages

 - Basic syntax
      ```python
        import x
        from x import y
        from x import y as z
      ```
 - Temminology for special methods: __<<method>>__
 - Method:
      - Python's basic tool for organizing code
      - Normally a single python source file
      - Load modules with `import`
      - Represent by module objects

## Structure details

   ![alt text](./images/package.JPG)

## Packages Vs Modules

   ![alt text](./images/package-vs-module.JPG)


## Locating modules

   - Uses the sys.path
      - Searches for the list of directories
      - Searched in order in import
      - First match provides module
      - ImportError where there is no match found
   - PythonPath-> export PYTHONPATH='absolute-path-url'
       
       ![alt text](./images/python-path.JPG)

## PEP420 and __init__.py

   ![alt text](./images/__init__.JPG)


### Project MultiReader:

   - Read uncompressed text files
   - Read gzip-compressed files
   - Read bz2-compressed files