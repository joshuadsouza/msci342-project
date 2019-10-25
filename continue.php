<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
      integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div class="container" style="margin-top: 20%">
      <div class="row" style="margin-left: 29.5%;">
        <div class="col">
          <button
            type="button"
            class="btn btn-primary"
            onclick="window.location='./index.php'"
          >
            BACK
          </button>
        </div>
      </div>
      <div class="row">
        <div class="col" style="margin-top: 4%; margin-left: 30%;">
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="inputGroupFileAddon01"
                >Input Schedule Folder </span
              >
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="inputGroupFile01"
                aria-describedby="inputGroupFileAddon01"
              />
              <label
                class="custom-file-label"
                for="inputGroupFile01"
                style="width: 50%"
                >Choose Folder</label
              >
            </div>
          </div>
        </div>
      </div>
      <div class="row" style="margin-top: 5%">
        <div class="col" style="margin-left: 30%;">
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="inputGroupFileAddon01"
                >Map PDF Path</span
              >
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="inputGroupFile01"
                aria-describedby="inputGroupFileAddon01"
              />
              <label
                class="custom-file-label"
                for="inputGroupFile01"
                style="width: 50%"
                >Choose file</label
              >
            </div>
          </div>
        </div>
      </div>
      <div class="row" style="margin-top: 5%">
        <div class="col" style="margin-left: 30%;">
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="inputGroupFileAddon01"
                >Student Numbers</span
              >
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="inputGroupFile01"
                aria-describedby="inputGroupFileAddon01"
              />
              <label
                class="custom-file-label"
                for="inputGroupFile01"
                style="width: 50%"
                >Choose file</label
              >
            </div>
          </div>
        </div>
      </div>

      <div class="row" style="margin-top: 5%">
        <div class="col" style="margin-left: 30%;">
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="inputGroupFileAddon01"
                >Output PDF Folder Path</span
              >
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="inputGroupFile01"
                aria-describedby="inputGroupFileAddon01"
              />
              <label
                class="custom-file-label"
                for="inputGroupFile01"
                style="width: 50%"
                >Choose Folder</label
              >
            </div>
          </div>
        </div>
      </div>

      <div class="row" style="margin-top: 5%">
        <div class="col" style="text-align: center;">
          <button
            type="button"
            class="btn btn-primary"
            onclick="window.location='./complete.php'"
          >
            CONVERT TO PDFs
          </button>
        </div>
      </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bs-custom-file-input/dist/bs-custom-file-input.min.js"></script>
    <script>
      bsCustomFileInput.init();
    </script>
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
  </body>
</html>