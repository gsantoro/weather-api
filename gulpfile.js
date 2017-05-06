var gulp = require('gulp');


gulp.task('default', function() {
  // place code for your default task here
  console.log("default action")
});

var server = require('gulp-server-livereload');

gulp.task('webserver', function() {
  gulp.src('app')
    .pipe(server({
      livereload: true,
      directoryListing: false,
      open: true
    }));
});
