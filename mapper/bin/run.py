from AbstractMap import AbstractMap

if __name__ == '__main__':
    map = AbstractMap()
    map._match('10000_grantAbstracts.xlsx','neo4j_rare_disease_list.json', IDcol='Application_ID', TEXTcols=['Abstract'])
    # 'Condition','OfficialTitle','BriefTitle','BriefSummary','Keyword','ArmGroupDescription','DetailedDescription'
    # Order of list dictates weight