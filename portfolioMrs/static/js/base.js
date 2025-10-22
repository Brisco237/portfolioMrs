document.addEventListener("DOMContentLoaded", function() {
    var grid = document.querySelector('.grid');
    var msnry = new Masonry(grid, {
      itemSelector: '.grid-item',
      gutter:10,
      fitWidth: true
    });
});