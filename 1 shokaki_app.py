import streamlit as st
import random

st.title("医学英語道場")
st.write("医学生の、医学生による、医学生のためのアプリ")

all_words = {
    "消化器":[
    {"english": "gastroesophageal reflux disease", "japanese": "胃食道逆流症"},
    {"english": "esophagitis", "japanese": "食道炎"},
    {"english": "Barrett esophagus", "japanese": "バレット食道"},
    {"english": "esophageal varices", "japanese": "食道静脈瘤"},
    {"english": "esophageal cancer", "japanese": "食道癌"},
    {"english": "Mallory-Weiss syndrome", "japanese": "マロリー・ワイス症候群"},
    {"english": "achalasia", "japanese": "アカラシア"},
    {"english": "hiatal hernia", "japanese": "食道裂孔ヘルニア"},
    {"english": "dysphagia", "japanese": "嚥下障害"},
    {"english": "odynophagia", "japanese": "嚥下痛"},

    {"english": "gastritis", "japanese": "胃炎"},
    {"english": "acute gastritis", "japanese": "急性胃炎"},
    {"english": "chronic gastritis", "japanese": "慢性胃炎"},
    {"english": "Helicobacter pylori infection", "japanese": "ヘリコバクター・ピロリ感染症"},
    {"english": "peptic ulcer disease", "japanese": "消化性潰瘍"},
    {"english": "gastric ulcer", "japanese": "胃潰瘍"},
    {"english": "duodenal ulcer", "japanese": "十二指腸潰瘍"},
    {"english": "gastric cancer", "japanese": "胃癌"},
    {"english": "gastric adenocarcinoma", "japanese": "胃腺癌"},
    {"english": "gastroenteritis", "japanese": "胃腸炎"},

    {"english": "celiac disease", "japanese": "セリアック病"},
    {"english": "lactose intolerance", "japanese": "乳糖不耐症"},
    {"english": "malabsorption syndrome", "japanese": "吸収不良症候群"},
    {"english": "short bowel syndrome", "japanese": "短腸症候群"},
    {"english": "small bowel obstruction", "japanese": "小腸閉塞"},
    {"english": "bowel obstruction", "japanese": "腸閉塞"},
    {"english": "ileus", "japanese": "イレウス"},
    {"english": "intussusception", "japanese": "腸重積"},
    {"english": "volvulus", "japanese": "腸捻転"},
    {"english": "ischemic bowel disease", "japanese": "虚血性腸疾患"},

    {"english": "Crohn disease", "japanese": "クローン病"},
    {"english": "ulcerative colitis", "japanese": "潰瘍性大腸炎"},
    {"english": "inflammatory bowel disease", "japanese": "炎症性腸疾患"},
    {"english": "irritable bowel syndrome", "japanese": "過敏性腸症候群"},
    {"english": "infectious colitis", "japanese": "感染性腸炎"},
    {"english": "pseudomembranous colitis", "japanese": "偽膜性腸炎"},
    {"english": "microscopic colitis", "japanese": "顕微鏡的大腸炎"},
    {"english": "toxic megacolon", "japanese": "中毒性巨大結腸症"},
    {"english": "appendicitis", "japanese": "虫垂炎"},
    {"english": "appendiceal abscess", "japanese": "虫垂膿瘍"},

    {"english": "constipation", "japanese": "便秘"},
    {"english": "chronic constipation", "japanese": "慢性便秘"},
    {"english": "diarrhea", "japanese": "下痢"},
    {"english": "chronic diarrhea", "japanese": "慢性下痢"},
    {"english": "melena", "japanese": "黒色便"},
    {"english": "hematochezia", "japanese": "血便"},
    {"english": "occult gastrointestinal bleeding", "japanese": "潜在性消化管出血"},
    {"english": "diverticulosis", "japanese": "大腸憩室症"},
    {"english": "diverticulitis", "japanese": "憩室炎"},
    {"english": "colonic perforation", "japanese": "大腸穿孔"},

    {"english": "colon polyp", "japanese": "大腸ポリープ"},
    {"english": "adenomatous polyp", "japanese": "腺腫性ポリープ"},
    {"english": "hyperplastic polyp", "japanese": "過形成性ポリープ"},
    {"english": "familial adenomatous polyposis", "japanese": "家族性大腸腺腫症"},
    {"english": "juvenile polyposis syndrome", "japanese": "若年性ポリポーシス症候群"},
    {"english": "Peutz-Jeghers syndrome", "japanese": "ポイツ・ジェガース症候群"},
    {"english": "Lynch syndrome", "japanese": "リンチ症候群"},
    {"english": "colorectal cancer", "japanese": "大腸癌"},
    {"english": "colon cancer", "japanese": "結腸癌"},
    {"english": "rectal cancer", "japanese": "直腸癌"},

    {"english": "hemorrhoids", "japanese": "痔核"},
    {"english": "anal fissure", "japanese": "裂肛"},
    {"english": "perianal abscess", "japanese": "肛門周囲膿瘍"},
    {"english": "fistula-in-ano", "japanese": "痔瘻"},
    {"english": "rectal prolapse", "japanese": "直腸脱"},
    {"english": "proctitis", "japanese": "直腸炎"},
    {"english": "proctocolitis", "japanese": "直腸結腸炎"},
    {"english": "fecal impaction", "japanese": "糞便塞栓"},
    {"english": "fecal incontinence", "japanese": "便失禁"},
    {"english": "anorectal malformation", "japanese": "鎖肛・肛門直腸奇形"},

    {"english": "hepatitis", "japanese": "肝炎"},
    {"english": "acute hepatitis", "japanese": "急性肝炎"},
    {"english": "chronic hepatitis", "japanese": "慢性肝炎"},
    {"english": "hepatitis A", "japanese": "A型肝炎"},
    {"english": "hepatitis B", "japanese": "B型肝炎"},
    {"english": "hepatitis C", "japanese": "C型肝炎"},
    {"english": "autoimmune hepatitis", "japanese": "自己免疫性肝炎"},
    {"english": "alcoholic hepatitis", "japanese": "アルコール性肝炎"},
    {"english": "fatty liver", "japanese": "脂肪肝"},
    {"english": "nonalcoholic fatty liver disease", "japanese": "非アルコール性脂肪性肝疾患"},

    {"english": "nonalcoholic steatohepatitis", "japanese": "非アルコール性脂肪肝炎"},
    {"english": "cirrhosis", "japanese": "肝硬変"},
    {"english": "portal hypertension", "japanese": "門脈圧亢進症"},
    {"english": "ascites", "japanese": "腹水"},
    {"english": "hepatic encephalopathy", "japanese": "肝性脳症"},
    {"english": "spontaneous bacterial peritonitis", "japanese": "特発性細菌性腹膜炎"},
    {"english": "hepatorenal syndrome", "japanese": "肝腎症候群"},
    {"english": "hepatocellular carcinoma", "japanese": "肝細胞癌"},
    {"english": "liver failure", "japanese": "肝不全"},
    {"english": "fulminant hepatitis", "japanese": "劇症肝炎"},

    {"english": "jaundice", "japanese": "黄疸"},
    {"english": "cholestasis", "japanese": "胆汁うっ滞"},
    {"english": "primary biliary cholangitis", "japanese": "原発性胆汁性胆管炎"},
    {"english": "primary sclerosing cholangitis", "japanese": "原発性硬化性胆管炎"},
    {"english": "biliary atresia", "japanese": "胆道閉鎖症"},
    {"english": "choledocholithiasis", "japanese": "総胆管結石"},
    {"english": "cholelithiasis", "japanese": "胆石症"},
    {"english": "cholecystitis", "japanese": "胆嚢炎"},
    {"english": "cholangitis", "japanese": "胆管炎"},
    {"english": "gallbladder cancer", "japanese": "胆嚢癌"},

    {"english": "acute pancreatitis", "japanese": "急性膵炎"},
    {"english": "chronic pancreatitis", "japanese": "慢性膵炎"},
    {"english": "pancreatic insufficiency", "japanese": "膵外分泌不全"},
    {"english": "pancreatic pseudocyst", "japanese": "膵仮性嚢胞"},
    {"english": "pancreatic cancer", "japanese": "膵癌"},
    {"english": "pancreatic adenocarcinoma", "japanese": "膵管腺癌"},
    {"english": "cystic fibrosis", "japanese": "嚢胞性線維症"},
    {"english": "carcinoid tumor", "japanese": "カルチノイド腫瘍"},
    {"english": "gastrointestinal stromal tumor", "japanese": "消化管間質腫瘍"},
    {"english": "peritonitis", "japanese": "腹膜炎"}
],
"神経内科": [
    {"english": "stroke", "japanese": "脳卒中"},
    {"english": "ischemic stroke", "japanese": "脳梗塞"},
    {"english": "hemorrhagic stroke", "japanese": "脳出血"},
    {"english": "subarachnoid hemorrhage", "japanese": "くも膜下出血"},
    {"english": "transient ischemic attack", "japanese": "一過性脳虚血発作"},
    {"english": "epilepsy", "japanese": "てんかん"},
    {"english": "status epilepticus", "japanese": "てんかん重積状態"},
    {"english": "migraine", "japanese": "片頭痛"},
    {"english": "tension headache", "japanese": "緊張型頭痛"},
    {"english": "cluster headache", "japanese": "群発頭痛"},
    {"english": "Parkinson disease", "japanese": "パーキンソン病"},
    {"english": "parkinsonism", "japanese": "パーキンソニズム"},
    {"english": "essential tremor", "japanese": "本態性振戦"},
    {"english": "Huntington disease", "japanese": "ハンチントン病"},
    {"english": "amyotrophic lateral sclerosis", "japanese": "筋萎縮性側索硬化症"},
    {"english": "multiple sclerosis", "japanese": "多発性硬化症"},
    {"english": "neuromyelitis optica", "japanese": "視神経脊髄炎"},
    {"english": "Guillain-Barre syndrome", "japanese": "ギラン・バレー症候群"},
    {"english": "myasthenia gravis", "japanese": "重症筋無力症"},
    {"english": "Lambert-Eaton myasthenic syndrome", "japanese": "ランバート・イートン筋無力症候群"},
    {"english": "myopathy", "japanese": "ミオパチー"},
    {"english": "muscular dystrophy", "japanese": "筋ジストロフィー"},
    {"english": "Duchenne muscular dystrophy", "japanese": "デュシェンヌ型筋ジストロフィー"},
    {"english": "peripheral neuropathy", "japanese": "末梢神経障害"},
    {"english": "diabetic neuropathy", "japanese": "糖尿病性ニューロパチー"},
    {"english": "carpal tunnel syndrome", "japanese": "手根管症候群"},
    {"english": "Bell palsy", "japanese": "ベル麻痺"},
    {"english": "trigeminal neuralgia", "japanese": "三叉神経痛"},
    {"english": "facial nerve palsy", "japanese": "顔面神経麻痺"},
    {"english": "dementia", "japanese": "認知症"},
    {"english": "Alzheimer disease", "japanese": "アルツハイマー病"},
    {"english": "vascular dementia", "japanese": "血管性認知症"},
    {"english": "Lewy body dementia", "japanese": "レビー小体型認知症"},
    {"english": "frontotemporal dementia", "japanese": "前頭側頭型認知症"},
    {"english": "delirium", "japanese": "せん妄"},
    {"english": "meningitis", "japanese": "髄膜炎"},
    {"english": "encephalitis", "japanese": "脳炎"},
    {"english": "brain abscess", "japanese": "脳膿瘍"},
    {"english": "normal pressure hydrocephalus", "japanese": "正常圧水頭症"},
    {"english": "hydrocephalus", "japanese": "水頭症"},
    {"english": "brain tumor", "japanese": "脳腫瘍"},
    {"english": "glioblastoma", "japanese": "膠芽腫"},
    {"english": "vestibular schwannoma", "japanese": "前庭神経鞘腫"},
    {"english": "cerebral palsy", "japanese": "脳性麻痺"},
    {"english": "spinocerebellar degeneration", "japanese": "脊髄小脳変性症"},
    {"english": "ataxia", "japanese": "運動失調"},
    {"english": "vertigo", "japanese": "めまい"},
    {"english": "syncope", "japanese": "失神"},
    {"english": "restless legs syndrome", "japanese": "むずむず脚症候群"},
    {"english": "sleep apnea syndrome", "japanese": "睡眠時無呼吸症候群"}
],
"血液": [
        {"english": "anemia", "japanese": "貧血"},
        {"english": "iron deficiency anemia", "japanese": "鉄欠乏性貧血"},
        {"english": "megaloblastic anemia", "japanese": "巨赤芽球性貧血"},
        {"english": "hemolytic anemia", "japanese": "溶血性貧血"},
        {"english": "aplastic anemia", "japanese": "再生不良性貧血"},
        {"english": "sickle cell disease", "japanese": "鎌状赤血球症"},
        {"english": "thalassemia", "japanese": "サラセミア"},
        {"english": "glucose-6-phosphate dehydrogenase deficiency", "japanese": "G6PD欠損症"},
        {"english": "hereditary spherocytosis", "japanese": "遺伝性球状赤血球症"},
        {"english": "disseminated intravascular coagulation", "japanese": "播種性血管内凝固"},
        {"english": "hemophilia", "japanese": "血友病"},
        {"english": "von Willebrand disease", "japanese": "フォン・ヴィレブランド病"},
        {"english": "thrombocytopenia", "japanese": "血小板減少症"},
        {"english": "immune thrombocytopenic purpura", "japanese": "免疫性血小板減少性紫斑病"},
        {"english": "thrombotic thrombocytopenic purpura", "japanese": "血栓性血小板減少性紫斑病"},
        {"english": "leukemia", "japanese": "白血病"},
        {"english": "acute myeloid leukemia", "japanese": "急性骨髄性白血病"},
        {"english": "acute lymphoblastic leukemia", "japanese": "急性リンパ性白血病"},
        {"english": "chronic myeloid leukemia", "japanese": "慢性骨髄性白血病"},
        {"english": "lymphoma", "japanese": "リンパ腫"},
        {"english": "multiple myeloma", "japanese": "多発性骨髄腫"}
    ]
    
}

department = st.selectbox("科を選んでください", list(all_words.keys()))
words = all_words[department]

if "last_department" not in st.session_state:
    st.session_state.last_department = department

if "current_word" not in st.session_state:
    st.session_state.current_word=random.choice(words)

if st.session_state.last_department != department:
    st.session_state.current_word = random.choice(words)
    st.session_state.last_department = department

word=st.session_state.current_word

st.subheader("英語")
st.write(word["english"])

if st.button("意味を表示"):
    st.write("### 日本語")
    st.write(word["japanese"])

if st.button("次の単語"):
    st.session_state.current_word=random.choice(words)
    st.rerun()