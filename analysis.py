import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()

def load_responses():
    '''
        Load a dataframe of responses
    '''
    return pd.read_csv('covid_survey_responses.csv')

def analysis(df,fs_text=14,fs_axis=10):
    '''
        Make a basic plot
    '''
    fig, ax = plt.subplots(3,3,figsize=(12,20))

    # Distribution of 2019 meetings attendence
    ax[0,0].hist(df['num_pre_meetings'],bins=np.arange(-.5,11,1))
    ax[0,0].plot(df['num_pre_meetings'].mean(), ax[0,0].get_ylim()[1],'rv')
    ax[0,0].set_ylabel('Count',fontsize=fs_text)
    ax[0,0].set_xlabel('2019 Meetings',fontsize=fs_text)
    ticks = np.arange(0,11,2)
    labels = ticks.astype(str)
    labels[-1] ='10+'
    ax[0,0].set_xticks(ticks)
    ax[0,0].set_xticklabels(labels,fontsize=fs_axis)
    ax[0,0].tick_params(axis="y",labelsize=fs_axis)

    # Distribution of COVID meetings attendance
    ax[0,1].hist(df['covid_meetings'],bins=np.arange(-.5,11,1))
    ax[0,1].plot(df['covid_meetings'].mean(), ax[0,1].get_ylim()[1],'rv')
    ax[0,1].set_ylabel('Count',fontsize=fs_text)
    ax[0,1].set_xlabel('Virtual Meetings',fontsize=fs_text)
    ticks = np.arange(0,11,2)
    labels = ticks.astype(str)
    labels[-1] ='10+'
    ax[0,1].set_xticks(ticks)
    ax[0,1].set_xticklabels(labels,fontsize=fs_axis)
    ax[0,1].tick_params(axis="y",labelsize=fs_axis)

    # Distribution of COVID meetings Presented
    ax[0,2].hist(df['covid_present'],bins=np.arange(-.5,11,1))
    ax[0,2].plot(df['covid_present'].mean(), ax[0,2].get_ylim()[1],'rv')
    ax[0,2].set_ylabel('Count',fontsize=fs_text)
    ax[0,2].set_xlabel('Virtual Presentations',fontsize=fs_text)
    ticks = np.arange(0,11,2)
    labels = ticks.astype(str)
    labels[-1] ='10+'
    ax[0,2].set_xticks(ticks)
    ax[0,2].set_xticklabels(labels,fontsize=fs_axis)
    ax[0,2].tick_params(axis="y",labelsize=fs_axis)

    # Distribution of 2019 meetings cost
    ax[1,0].hist(df[~df['cost'].isnull()]['cost'])
    ax[1,0].plot(df[~df['cost'].isnull()]['cost'].mean(), ax[1,0].get_ylim()[1],'rv')
    ax[1,0].set_ylabel('$/meeting (USD)',fontsize=fs_text)
    ax[1,0].set_xlabel('2019 Cost',fontsize=fs_text)
    ax[1,0].tick_params(axis="y",labelsize=fs_axis)
    ax[1,0].tick_params(axis="x",labelsize=fs_axis)

    # Virtual Attendance Quality
    ax[1,1].hist(df['meeting_quality'],bins=np.arange(-.5,11,1))
    ax[1,1].plot(df['meeting_quality'].mean(), ax[1,1].get_ylim()[1],'rv')
    ax[1,1].set_ylabel('Count',fontsize=fs_text)
    ax[1,1].set_xlabel('Virtual Attendance \n Quality',fontsize=fs_text)
    ticks = np.arange(0,11,2)
    labels = ticks.astype(str)
    labels[-1] ='10+'
    ax[1,1].set_xticks(ticks)
    ax[1,1].set_xticklabels(labels,fontsize=fs_axis)
    ax[1,1].tick_params(axis="y",labelsize=fs_axis)


    # Virtual Presentation Quality
    ax[1,2].hist(df['present_quality'],bins=np.arange(-.5,11,1))
    ax[1,2].plot(df['present_quality'].mean(), ax[1,2].get_ylim()[1],'rv')
    ax[1,2].set_ylabel('Count',fontsize=fs_text)
    ax[1,2].set_xlabel('Virtual Presentation \n Quality',fontsize=fs_text)
    ticks = np.arange(0,11,2)
    labels = ticks.astype(str)
    labels[-1] ='10+'
    ax[1,2].set_xticks(ticks)
    ax[1,2].set_xticklabels(labels,fontsize=fs_axis)
    ax[1,2].tick_params(axis="y",labelsize=fs_axis)

    def func(pct, labels):
        return labels.pop()

    # Distribution of COVID meetings Presented
    labels = ['No','Cultural','Format','Yes']
    wedges, texts, autotext = ax[2,0].pie(df['post_attend'].value_counts(),autopct = lambda pct: func(pct,labels),textprops=dict(color='w',fontsize=12))
    ax[2,0].legend(wedges, df['post_attend'].value_counts().index, title='Post-COVID are you more likely to attend virtually?',loc='lower center',bbox_to_anchor=[0.5,-.7])

    # Distribution of COVID meetings Presented
    labels = ['Depends','Yes'] 
    wedges, texts, autotext = ax[2,1].pie(df['post_options'].value_counts(),autopct = lambda pct: func(pct,labels),textprops=dict(color='w',fontsize=12))
    ax[2,1].legend(wedges, df['post_options'].value_counts().index, title='Post-COVID do you want \nmore virtual options?',loc='lower center',bbox_to_anchor=[0.5,-.7])

    # Distribution of COVID meetings Presented
    labels = ['No','In the future','Yes'] 
    wedges, texts, autotext = ax[2,2].pie(df['climate'].value_counts(),autopct = lambda pct: func(pct,labels),textprops=dict(color='w',fontsize=12))
    ax[2,2].legend(wedges, df['climate'].value_counts().index, title='Is carbon footprint a factor \nin attending a conference?',loc='lower center',bbox_to_anchor=[0.5,-.7])
    plt.tight_layout()

