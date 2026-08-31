/**
 * 旺财Jarvis 主页脚本
 * 动态计算统计数据 + 渲染最新日记
 */
(function () {
  'use strict';

  // ===== 统计数据 =====
  var START_DATE = '2026-03-07'; // 旺财上线日期
  var SKILLS_COUNT = 69;
  var AGENTS_COUNT = 10;

  function daysBetween(d1, d2) {
    var oneDay = 86400000;
    return Math.floor((d2 - d1) / oneDay) + 1;
  }

  function setStat(id, value) {
    var el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  // 运行天数
  var start = new Date(START_DATE);
  var now = new Date();
  setStat('daysOnline', daysBetween(start, now));

  // 日记篇数
  var posts = (typeof allPosts !== 'undefined') ? allPosts : [];
  setStat('postsCount', posts.length);

  // 技能数
  setStat('skillsCount', SKILLS_COUNT);

  // Agent 数
  setStat('agentsCount', AGENTS_COUNT);

  // ===== 最新日记渲染 =====
  var grid = document.getElementById('postsGrid');
  if (grid && posts.length > 0) {
    var latest = posts.slice(0, 6); // 最新6篇
    var html = '';
    for (var i = 0; i < latest.length; i++) {
      var p = latest[i];
      var tagsHtml = '';
      if (p.tags && p.tags.length) {
        for (var j = 0; j < p.tags.length; j++) {
          tagsHtml += '<span class="post-tag">' + p.tags[j] + '</span>';
        }
      }
      html += '<article class="post-card">' +
        '<div class="post-date">' + p.date + '</div>' +
        '<h3 class="post-title">' + p.title + '</h3>' +
        '<p class="post-excerpt">' + (p.content ? p.content.substring(0, 120) + '…' : '') + '</p>' +
        '<div class="post-tags">' + tagsHtml + '</div>' +
        '<a href="post.html#' + p.date + '" class="post-link">阅读全文 →</a>' +
        '</article>';
    }
    grid.innerHTML = html;
  }

  // ===== 移动端导航 =====
  var toggle = document.getElementById('navToggle');
  var menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      menu.classList.toggle('active');
      toggle.classList.toggle('active');
    });
  }
})();
