---
layout: default
title: 동민의 개발 블로그
---

# 👋 환영합니다!

Unity, DX12, Unreal 관련 학습 노트를 정리한 공간입니다. 아래에서 주제별 글을 확인해보세요.

## 📚 학습 정리 페이지

{% for page in site.pages %}
  {% if page.path contains 'study/' and page.title and page.url != '/study/index.html' %}
- [{{ page.title }}]({{ page.url }})
  {% endif %}
{% endfor %}
