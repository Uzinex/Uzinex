import { useTranslation } from 'react-i18next';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { motion } from 'framer-motion';
import PageWrapper from '../components/PageWrapper';

const Home = () => {
  const { t } = useTranslation();

  return (
    <PageWrapper>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
        <Navbar />

        <motion.section id="intro" className="hero" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
          <h1>{t('home.title')}</h1>
          <p className="subtitle">{t('home.subtitle')}</p>
          <a href="#projects" className="cta">{t('home.cta')}</a>
        </motion.section>

        <motion.section id="features" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5, delay: 0.1 }}>
          <h2>{t('home.featuresTitle')}</h2>
          <ul className="features-list">
            <li>{t('home.features.blockchain')}</li>
            <li>{t('home.features.ai')}</li>
            <li>{t('home.features.cyber')}</li>
          </ul>
        </motion.section>

        <motion.section id="projects" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5, delay: 0.2 }}>
          <h2>{t('projects.title')}</h2>
          <div className="project-links">
            <a href="https://uzcoin.uzinex.uz">{t('home.projects.uzcoin')}</a>
            <a href="https://freelance.uzinex.uz">{t('home.projects.freelance')}</a>
            <a href="https://host.uzinex.uz">{t('home.projects.host')}</a>
            <a href="https://bank.uzinex.uz">{t('home.projects.bank')}</a>
          </div>
        </motion.section>

        <motion.section id="contact" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5, delay: 0.2 }}>
          <h2>{t('navbar.contact')}</h2>
          <p><a href="https://t.me/uzinex">{t('contact.telegram')}</a></p>
          <p><a href="https://threads.net/@uzinex_official">{t('contact.threads')}</a></p>
          <p>{t('contact.email')}: info@uzinex.uz</p>
        </motion.section>

        <Footer />
      </motion.div>
    </PageWrapper>
  );
};

export default Home;
