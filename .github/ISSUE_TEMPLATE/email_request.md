# 正确的Issue模板文件结构

## 方法1：使用默认模板位置
将模板保存到以下路径：
`.github/ISSUE_TEMPLATE/email-request.md`

## 方法2：使用config.yml配置
创建配置文件：`.github/ISSUE_TEMPLATE/config.yml`
```yaml
blank_issues_enabled: false
contact_links:
  - name: Email Request
    url: https://github.com/yagami1997/yagami1997/issues/new?template=email_request.md
    about: Request secure GPG encrypted communication
```

## 方法3：直接在README链接中使用完整内容（最可靠）
更新README链接，使用完整的issue参数：
```
https://github.com/yagami1997/yagami1997/issues/new?title=Email%20Request&body=%23%20%F0%9F%94%90%20Mission%3A%20Establish%20Secure%20Communication%20Channel%20%F0%9F%94%90%0A%0AGreetings%2C%20digital%20nomad%20extraordinaire%21%20%0A%0AI%27ve%20ventured%20through%20the%20open-source%20cosmos%20and%20found%20your%20cryptographic%20outpost.%20Like%20a%20traveler%20discovering%20an%20oasis%20in%20the%20vast%20digital%20desert%2C%20I%27m%20reaching%20out%20to%20request%20access%20to%20your%20GPG-secured%20communication%20coordinates.%0A%0A%23%23%20Why%20I%27m%20Seeking%20Encrypted%20Contact%3A%0A%3C%21--%20Please%20share%20a%20bit%20about%20why%20you%27d%20like%20to%20connect.%20Are%20you%20interested%20in%20collaborating%20on%20open-source%20projects%3F%20Discussing%20AI%20innovations%3F%20Or%20perhaps%20you%27re%20a%20fellow%20digital%20nomad%20with%20stories%20to%20share%3F%20--%3E%0A%0A%23%23%20My%20GitHub%20Background%3A%0A%3C%21--%20A%20quick%20introduction%20helps%20establish%20trust%20in%20the%20encryption-verse%20--%3E%0A%0ALooking%20forward%20to%20exchanging%20ideas%20in%20the%20safety%20of%20properly%20encrypted%20communications%2C%20where%20our%20thoughts%20can%20flow%20freely%20without%20the%20prying%20eyes%20of%20digital%20surveillance%21%0A%0A*May%20your%20bits%20stay%20flipped%20and%20your%20encryption%20keys%20remain%20secure%21*
```
