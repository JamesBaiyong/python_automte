#coding=utf-8
'''
创建35份50个美国州的首府问答卷，且每一份问答题是随机的
'''
import random,os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
#创建35份问卷以及每份问卷的答案

	dir = 'Quize&Answer'
	if not os.path.exists(dir):
		os.mkdir(dir)

	quizFile = open('%s/capitalsquiz%s.txt'%(dir,quizNum +1 ),'w')
	answerKeyFile = open('%s/capitalsquiz_answers%s.txt'%(dir,quizNum + 1 ),'w')

	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write(('--'*20)+'State Capitals Quiz (From %s)'%(quizNum +1)+('--'*20))
	quizFile.write('\n\n')

	states = list(capitals.keys()) #把50个州名写入states列表
	random.shuffle(states)

	for questionNum in range(50):
		#在每份问卷中写入问答题

		correntAnswer = capitals[states[questionNum]] #按照州的名字在字典capitals中找到正确答案
		wrongAnswers = list(capitals.values()) #写入所有答案
		del wrongAnswers[wrongAnswers.index(correntAnswer)]#设置错误答案，即把正确答案删除
		wrongAnswers = random.sample(wrongAnswers,3)#在里列表中随机写入指定列表，指定长度的片段
		answerOptions = wrongAnswers+[correntAnswer]
		random.shuffle(answerOptions)#打乱指定列表中的元素

		quizFile.write('%s.What is the capital of %s?\n'
		               %(questionNum +1 ,states[questionNum]))
		for i in range(4):
			quizFile.write('%s.%s\n'
			               %('ABCD'[i],answerOptions[i]))
		quizFile.write('\n')

		answerKeyFile.write('%s.%s\n'
		                    %(questionNum + 1,'ABCD'[answerOptions.index(correntAnswer)]))
	quizFile.close()
	answerKeyFile.close()