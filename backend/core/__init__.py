"""
core 模組初始化
"""

from .word_processor import (
    remove_content_controls,
    paragraph_to_html_with_links,
    table_to_html,
    is_pure_url,
    extract_embed_url,
    convert_url_to_iframe
)

from .html_converter import (
    apply_auto_toc_and_smooth,
    docx_to_html_with_links
)

from .image_processor import process_image

__all__ = [
    'remove_content_controls',
    'paragraph_to_html_with_links',
    'table_to_html',
    'is_pure_url',
    'extract_embed_url',
    'convert_url_to_iframe',
    'apply_auto_toc_and_smooth',
    'docx_to_html_with_links',
    'process_image'
]
