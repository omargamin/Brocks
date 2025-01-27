from setuptools import setup, find_packages

setup(
    name='brocks',  # اسم المكتبة
    version='0.1',  # النسخة الأولى للمكتبة
    packages=find_packages(),  # تحديد كل الحزم (المجلدات) في المشروع
    install_requires=[  # قائمة المكتبات الخارجية المطلوبة (لو في مكتبات خارجية)
        # مثال: 'numpy',
    ],
    author='اسمك',  # اسم المؤلف
    author_email='بريدك الإلكتروني',  # البريد الإلكتروني للمؤلف
    description='وصف قصير للمكتبة',  # وصف مختصر للمكتبة
    long_description=open('README.md').read(),  # الوصف الكامل من ملف README.md
    long_description_content_type='text/markdown',  # نوع الوصف في README
    url='رابط المستودع على GitHub أو أي رابط آخر',  # رابط مستودع الكود على GitHub أو الموقع الرسمي
    classifiers=[  # قائمة التصنيفات الخاصة بالمكتبة
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # تحديد الحد الأدنى لإصدار Python
)
