def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv','.xlsx', '.xls']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension. Try CSV, XLS, XLSX, or paste data.')