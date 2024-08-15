$(document).ready(function() {
    // Event listener for edit button clicks
    $('.edit').on('click', function() {
        // Get data attributes from the selected table row
        var title = $(this).data('title');
        var brand = $(this).data('brand');
        var category = $(this).data('category');
        var description = $(this).data('description');
        var price = $(this).data('price');
        var qty = $(this).data('qty'); 

        // Populate the form fields with the selected data
        $('#title').val(title);
        $('#brand').val(brand);
        $('#category').val(category);
        $('#description').val(description);
        $('#price').val(price);
        $('#qty').val(qty);
    });
});