const {
  Chromeless
} = require('chromeless');

async function run() {
  const chromeless = new Chromeless();

  const screenshot = await chromeless
    // 打开百度
    .goto('https://www.baidu.com')
    // 定位name为wd的输入框，并输入chromeless
    .type('chromeless', 'input[name="wd"]')
    // 点击id为su 元素
    .click('#su')
    // 等待 id为content_left元素加载
    .wait('#content_left')
    // 截图
    .screenshot();
  // 打印本地文件路径或者S3 URL
  console.log(screenshot);
  // 结束
  await chromeless.end()
}

run().catch(console.error.bind(console));
