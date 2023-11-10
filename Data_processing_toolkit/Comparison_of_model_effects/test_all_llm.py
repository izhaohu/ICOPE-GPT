import use_chatglm2 as ch2
import pandas as pd

url = "http://192.168.11.33:7861/chat"
url2 = "http://192.168.11.33:7861/local_doc_qa/local_doc_chat"
headers = {"Content-Type": "application/json"}
data_all=[]
data = {
  "knowledge_base_id":"tjl",
  "question": "对于拒绝食物的老人，如何确保老人的营养和饮食需求得到满足？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "帕金森老人服用盐酸罗匹尼罗，一天内服用了40mg是否超出了使用剂量？会出现哪些不良反应？",
  "history": [],
  "type":"药师咨询"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "得了癌症的老人突然变得难以应对、脾气暴躁，想离家出走，可能是什么原因？该如何处理？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "如何判断阿尔兹海默症的老人有摔倒的风险，可以从日常生活中的哪些细节中发现老人存在跌倒的风险？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "老人的家属和老人的意愿不一致时该怎么办？例如老人希望多出去走走，看看世界；而家人出于安全的考虑希望老人每天在呆在家里。",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "老人得了急性应激障碍，该怎么护理？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)


data = {
  "knowledge_base_id":"tjl",
  "question": "如果你发现一个老人在我们的设施中遭受虐待或不公平对待，作为照护人员该怎么处理？",
  "history": [],
  "type":"照护管理"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "我无论问老人什么问题，他都回答：【啊啊依依啊啊依依啊啊依依】，从老人的回答中能否判断他得了认知障碍？可能是什么疾病？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "长期卧床的认知症老人有什么康复方法能能提高他的活动能力，甚至让他重新站起来，回归社会？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "一位患者出现了持续性的胀痛和黄疸，经影像学检查后确诊为肝胆管结石病，应该采取哪些治疗方案？",
  "history": [],
  "type":"照护知识"
}
data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "请根据下面的文本生成摘要，生成的摘要格式为："
              "病人症状：内容\n;病史信息：内容\n;既往症：内容\n;诊断：内容\n;检查建议：内容\n;用药建议：内容\n;。"
              "文本为：\n\n"
              "{医生：您好，请问您有什么不舒服的地方需要咨询吗？患者：我有反复的上腹部疼痛已经有3年了，最近3个月症状更加严重。"
              "医生：能具体描述一下疼痛的性质吗？患者：隐约的疼,不是特别剧烈。"
              "医生：疼痛与吃饭有关系吗？有没有感觉饥饿或者餐后疼痛会加剧?患者：一般吃完饭疼的会更厉害。"
              "医生：除了上腹痛，还有其他表现吗?患者：反酸、嗳气。"
              "医生：好的，您是否有发热、黄疸、呕血或者黑便的情况？患者：没有，这些症状我都没有出现过。"
              "医生：出现这种情况后去医院看过吗？患者：在当地诊所看过，开了吗丁啉。"
              "医生：用药后疗效如何？患者：腹痛会缓解一些。"
              "医生：在您家族中，是否有人有高血压的病史？患者：我父亲有高血压的病史。"
              "医生：好的，最后我想问一下，您是否有过敏史？患者：没有，我没有任何过敏史。"
              "医生：根据您的症状和病史，我初步怀疑您可能患有慢性胃炎。为了更好地了解您的情况，我建议您进行大便潜血和胃镜检查。}",
  "history": [],
  "type":"生成病例(多轮对话测试)"
}
data_all.append(data)
data = {
  "knowledge_base_id":"tjl",
  "question": "你是一位专业的医生，针对下面的问诊信息，你会推荐患者做哪些检查呢？并解释你为什么要做这些检查？问诊信息为：\n\n"
    "{患者：我最近发热、咳嗽，还有咳红色痰，而且右侧胸痛，已经持续两天了。医生：是否有其他不适感觉？比如头痛、乏力、呼吸困难等？"
    "患者：没有头痛和乏力，但有点呼吸急促。医生：除了胸痛，你还有其他部位的疼痛吗，比如腹痛或关节痛？"
    "患者：没有其他部位的疼痛，只有右侧胸痛。医生：你有没有感觉呼吸困难加重或者活动时加重的情况？"
    "患者：我感觉呼吸困难在咳嗽时会加重一些。医生：你之前起病前有没有受到雨淋或者湿冷环境的暴露？"
    "患者：我确实遭雨淋了。医生：有没有血丝或血块混在痰中？"
    "患者：没有血丝或血块混在痰中，只是像是铁锈色的痰。医生：除了这次的症状，你还有患过其他慢性病的历史吗，比如高血压、糖尿病等？"
    "患者：没有。医生：你是否曾经患过肝炎或结核等传染病？"
    "患者：没有。医生：你有没有最近进行过手术或遭受外伤？"
    "患者：没有。医生：之前检查过吗？"
    "患者：不好意思，没有。医生：你有没有其他家族成员或同事朋友有相似的症状？"
    "患者：没有，我是唯一出现这些症状的人。医生：你最近有没有接触过有呼吸道感染病史的人？"
    "患者：没有。医生：你有没有吸烟或酗酒的习惯？"
    "患者：没有，我从来不吸烟和酗酒。}",
  "history": [],
  "type":"检查推荐(多轮对话测试)"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "根据以下患者的情况，给出该患者应该去做的检查检验项目，并给出推荐原因。患者病情：女性，黑便、呕血",
  "history": [],
  "type":"检查推荐"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "请模拟一名药师给我推荐处方：根据患者的年龄、性别、孕哺情况、临床诊断，给该患者推荐合理的处方，包括药品名称、规格、数量、用法用量。患者病情：7岁，男性，确诊为胃肠型感冒",
  "history": [],
  "type":"处方推荐"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "我是一名医生，你来扮演一名哮喘急性发作患者，我们来模拟一场问诊，我想通过这样的模拟来锻炼我的接诊能力。您觉得哪里不舒服？",
  "history": [],
  "type":"医生培训"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "请模拟一个心理医生，针对患者的问题进行心理安慰：我最近脾气很暴躁。",
  "history": [],
  "type":"心理咨询"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "碘酒可以和红药水一起使用吗？",
  "history": [],
  "type":"药师咨询"
}

data_all.append(data)



data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【白天饮食状态差精神不佳，下午17:09测体温37度4，测血压151/77毫米汞柱，脉搏74，血氧96，已告知家属并进行物理降温。】",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【长者既往高血压，脑梗病史。长者于2023年6月3日长者发生过抽搐。经处理后好转。6月13日11点左右长者家属为长者吃了一颗安宫牛黄丸。17:00长者再次突发抽搐，立即通知家属并测量生命体征。血压：172/71mmhg，心率：95次/分。应家属要求立即服用一片降压药。并安抚长者后状态有所好转。】",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【长者近几天，血糖偏高，饮食时偶有呕吐现象，联系家属，家属来门店，私家车接长者去住院治疗，现住院中。长者认知功能障碍，吞咽功能减弱。】？",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【长者既往有帕金森综合征，前列腺炎，血管性PD病史。神清，轮椅代步。长者于14:44分在床边滑落。询问无不适，查体无异常。生命体征正常。血压：137/84mmhg，心率：104次/分，血氧：94%。】",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【长者既往有多发性脑梗死，高血压三级，大脑中动脉狭窄，颈内动脉狭窄。轮椅代步。于6月5日早上发现长者右脚大拇指指甲内侧红肿，疑似甲沟炎。告知家属后家属叫来修甲师为长者处理。】",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【骶尾部有轻度破溃，直径1cm。身上有天疱疮。该长者免疫力低下，身上长了天疱疮，身体瘦弱，皮肤腰臀处破溃面较多，已通知家属，医生每周四给老人注射提高免疫力的药剂。】",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "当老人出现以下情况怎么办？老人的情况描述如下：【该老人右脚浮肿较重，右脚面有小的破溃，二三脚趾之间有脚气。老人情绪不稳定，经常坐着活动较少，下肢循环不畅，加之心脏及肾功能功能减退，导致下肢浮肿】",
  "history": [],
  "type":"萤火虫事件"
}

data_all.append(data)



data = {
  "knowledge_base_id":"tjl",
  "question": "在上海，什么情况下可以申请重度残疾人护理补贴？",
  "history": [],
  "type":"照护政策"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "《上海市基本养老服务清单（2023年版）》的主要内容是什么？",
  "history": [],
  "type":"照护政策"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "给我药品{盐酸伐昔洛韦颗粒}的国药准字、药品名、生产厂家、规格、适应症、禁忌、药物相互作用、用法用量、适应症、不良反应",
  "history": [],
  "type":"药师咨询"
}
data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "上海㐄麑靡游乐园的具体地址是哪里？",
  "history": [],
  "type":"测试用"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "上海㐄麑靡游乐园的企业法人是谁？",
  "history": [],
  "type":"测试用"
}

data_all.append(data)

data = {
  "knowledge_base_id":"tjl",
  "question": "2023年7月18日上海的天气怎么样？",
  "history": [],
  "type":"测试用"
}
data_all.append(data)



#结果res
res=pd.DataFrame()
#保存问题
question_list=[]
answer_list=[]
answer_list2=[]
type_list=[]
history_list=[]

def uselora():
  for i in data_all:
    #print(i['question'])
    data = {"knowledge_base_id": "tjl","question": i['question'],"history": []}
    question_list.append(i['question'])
    type_list.append(i['type'])
    history_list.append(str(i['history']))
    responses=ch2.chat(url,headers,data)
    print(responses)
    answer_list.append(responses.json()["response"])

  res["问题"]=pd.Series(question_list)
  res["type"] = pd.Series(type_list)
  res["聊天历史"]=pd.Series(history_list)
  res["回答_Lora微调_不用知识库"]=pd.Series(answer_list)
#
  for i in data_all:
    #print(i['question'])
    data = {"knowledge_base_id": "tjl","question": i['question'],"history": []}
    #question_list.append(i['question'])
    responses=ch2.chat_knowledge(url2,headers,data)
    print(responses)
    answer_list2.append(responses.json()["response"]+'\n'+str(responses.json()['source_documents']))
  res["回答_Lora微调_用知识库"]=pd.Series(answer_list2)

  res.to_csv('问答效果对比.csv', index=False, encoding='utf-8-sig')
def notuselora():
  for i in data_all:
    #print(i['question'])
    data = {"knowledge_base_id": "tjl","question": i['question'],"history": []}
    question_list.append(i['question'])
    type_list.append(i['type'])
    history_list.append(str(i['history']))
    responses=ch2.chat(url,headers,data)
    print(responses)
    answer_list.append(responses.json()["response"])
  res["问题"]=pd.Series(question_list)
  res["type"] = pd.Series(type_list)
  res["聊天历史"] = pd.Series(history_list)
  res["回答_不用Lora微调_不用知识库"]=pd.Series(answer_list)
  #

  for i in data_all:
    #print(i['question'])
    data = {"knowledge_base_id": "tjl","question": i['question'],"history": []}
    #question_list.append(i['question'])
    responses=ch2.chat_knowledge(url2,headers,data)
    print(responses)
    answer_list2.append(responses.json()["response"]+'\n'+str(responses.json()['source_documents']))
  res["回答_不用Lora微调_用知识库"]=pd.Series(answer_list2)

  res.to_csv('问答效果对比2.csv', index=False, encoding='utf-8-sig')


if __name__ == "__main__":
  uselora()
  #notuselora()
  print("success")
