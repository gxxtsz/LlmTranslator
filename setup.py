from setuptools import setup, find_packages

setup(
    name='LlmTranslator',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    version='0.1.0',
    description='A translator using LLM',
    author='gxxtsz',
    author_email='2460726476@qq.com',
    url='https://github.com/gxxtsz/LlmTranslator',
    # 可按需添加依赖
    install_requires=[
        'requests',
    ],
)
