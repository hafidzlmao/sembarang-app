import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Sembarang from '../components/sembarang'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => { 
  return (
    <div className={styles.container}>
      <Head>
        <title>Sembarang | Branding and Marketing Generator using AI</title>
        <meta name="description" content="Genarate your product a branding snippet and Keywords" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <Sembarang/>
    </div>
  )
}

export default Home
