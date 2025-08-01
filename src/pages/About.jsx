import { useTranslation } from 'react-i18next';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { motion } from 'framer-motion';
import PageWrapper from '../components/PageWrapper';

const About = () => {
  const { t } = useTranslation();

  return (
    <PageWrapper>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      >
        <Navbar />
        <motion.section id="about" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
          <h1>{t('about.title')}</h1>
          <p>{t('about.description')}</p>
        </motion.section>
        <motion.section id="mission" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5, delay: 0.1 }}>
          <h2>{t('about.missionTitle')}</h2>
          <p>{t('about.mission')}</p>
        </motion.section>
        <motion.section id="directions" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5, delay: 0.2 }}>
          <h2>{t('about.directionsTitle')}</h2>
          <ul>
            <li>{t('about.directions.software')}</li>
            <li>{t('about.directions.cyber')}</li>
            <li>{t('about.directions.blockchain')}</li>
            <li>{t('about.directions.ai')}</li>
            <li>{t('about.directions.defense')}</li>
            <li>{t('about.directions.fintech')}</li>
          </ul>
        </motion.section>
        <motion.section id="philosophy" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5, delay: 0.3 }}>
          <h2>{t('about.philosophyTitle')}</h2>
          <ul>
            <li>{t('about.philosophy.sovereignty')}</li>
            <li>{t('about.philosophy.zeroTrust')}</li>
            <li>{t('about.philosophy.aiFirst')}</li>
            <li>{t('about.philosophy.openWorld')}</li>
          </ul>
        </motion.section>
        <Footer />
      </motion.div>
    </PageWrapper>
  );
};

export default About;
